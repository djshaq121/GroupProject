// Copyright 

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "WeaponBase.h"
#include "Runtime/Engine/Classes/Animation/AnimInstance.h"


// Sets default values
AWeaponBase::AWeaponBase()
{

	bIsEquipped = false;
	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	CollisonSphere = CreateDefaultSubobject<USphereComponent>(TEXT("CollisonSphere"));
	RootComponent = CollisonSphere;
	WeaponMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("GunMesh"));
	WeaponMesh->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);

	TraceParams = FCollisionQueryParams(FName(TEXT("Projectile Trace'")), true, this);


	NoEquipAnimDuration = 0.5f;

}

// Called when the game starts or when spawned
void AWeaponBase::BeginPlay()
{
	Super::BeginPlay();
	if (bCanInteract)
	{
		CollisonSphere->OnComponentBeginOverlap.AddDynamic(this, &AWeaponBase::OnPlayerEnterPickupBox);
	}

	CurrentAmmoInClip = MaxAmmoPerClip;
	CurrentAmmoInGun = MaxAmmoInGun;
}

/*PickUp*/

// Called every frame
void AWeaponBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

class APlayerCharacter* AWeaponBase::GetPawnOwner() const
{
	auto playerpawn = GetWorld()->GetFirstPlayerController()->GetPawn();
	if (!playerpawn) { return nullptr; }

	return Cast<APlayerCharacter>(playerpawn);
}


void  AWeaponBase::DealDamage(const FHitResult& Hit)
{

	if (!ensure(GetPawnOwner())) { return; }

	//Check to see if we hit and actor again

	if (Hit.GetActor())
	{
		float DealtDamage = BaseDamage;//Later maybe damage multipler 
		FVector ShotDirection = GetActorLocation() - Hit.ImpactPoint;//Gets the location of the gun subtract from the hit point location to find the direction

																	 //This fully describes the damage recieved 
		FPointDamageEvent DamageEvent;
		DamageEvent.Damage = DealtDamage;
		DamageEvent.HitInfo = Hit;
		DamageEvent.ShotDirection = ShotDirection;
		DamageEvent.ShotDirection.Normalize();

		//Calls the method on the actor that takes damage
		/*Crashes if the player is still shooting, hits an actor and dies */

		Hit.GetActor()->TakeDamage(DealtDamage, DamageEvent, GetPawnOwner()->GetController(), this);//Crashes at this line

																									//When the above line is commented, it Continues to shoot even when im dead. 
																									//Had a problem were if the player look down or up they could shoot themselves. Fixed by using custom preset on player
	}


}

FName AWeaponBase::GetWeaponName() const
{
	return WeaponName;
}

/*The method that is called in weapon class*/
void  AWeaponBase::StartFire()
{
	if (GetPawnOwner() != nullptr && !GetPawnOwner()->GetIsDead())//Stops the game from crashing when the player shoots and dies at the same time  
	{
		if (CurrentAmmoInClip > 0 && bCanFire)
		{
			if (WeaponFireShake)//Checking if we have 
			{
				//This oscillates the camera 
				GetWorld()->GetFirstPlayerController()->ClientPlayCameraShake(WeaponFireShake, 1.f);
			}

			Recoil();
			bIsFiring = true;
			DoFire();

			float TimerDelay = FireRate > 0 ? 1 / (FireRate*0.01667) : FApp::GetDeltaTime();

			auto World = GetWorld();
			if (World) {
				//This what makes the doFire loop when its held down

				if (!FireRateHandle.IsValid())
				{
					World->GetTimerManager().SetTimer(FireRateHandle, this, &AWeaponBase::StartFire, TimerDelay, true);//This will loop the startfire because we set it to true

				}
			}
			else {

				StopFire();

			}
		}
		//This reloads when the ammo reaches zero
		if (CurrentAmmoInClip <= 0 && CurrentAmmoInGun > 0 && GetCanReload()) {
			StopFire();
			StartReload(); 
		}
	}




}
void  AWeaponBase::StopFire()
{
	bIsFiring = false;
	GetWorld()->GetTimerManager().ClearTimer(FireRateHandle);
	FireRateHandle.Invalidate();
}

void  AWeaponBase::DoFire()
{
	SpawnMuzzleEffect();
	FHitResult Hit = FHitResult();
	FVector Start;


	UseAmmo();


	if (GetSightRayHitLocation(Hit))
	{
		auto HitLocation = Hit.Location;
		//Checks if we hit something
		if (Hit.bBlockingHit) {

			SpawnImpactEffect(Hit);	//If we hit something spawn at effect at impact point
			SpawnTrailEffect(Hit.ImpactPoint);

		}
		else
		{

			//TODO - Fix the trace effect when shooting into the distance
			FVector ImpactPoint = Hit.ImpactPoint;
			auto muzzle = WeaponMesh->GetSocketLocation("MuzzleSocketName");
			FVector AimDir = (Hit.TraceEnd - muzzle).GetSafeNormal();
			FVector EndTrace = muzzle + (AimDir * WeaponRange);

			SpawnTrailEffect(EndTrace);
		}

	}

	if (Hit.GetActor())
	{
		//UE_LOG(LogTemp, Warning, TEXT("Actor hit: %s "), *Hit.GetActor()->GetName());
		//Calls DealDamage passing the actor we hit
		DealDamage(Hit);

	}
}

bool AWeaponBase::GetSightRayHitLocation(FHitResult &HitResult) const

{
	//Find the crosshair position in pixel coordinate

	int32 ViewportSizeX, ViewportSizeY;

	//Gets the size of the view port
	GetWorld()->GetFirstPlayerController()->GetViewportSize(ViewportSizeX, ViewportSizeY);
	auto ScreenLocation = FVector2D(ViewportSizeX *  CrossHairXLocation, ViewportSizeY *  CrossHairYLocation);



	FVector LookDirection;// Out Parameter
						  //De-Project the screen position of the crosshair to a world direction
	if (GetLookDirection(ScreenLocation, LookDirection))
	{
		//Line trace along the look direction 
		GetLookVectorHitLocation(LookDirection, HitResult);
	}

	return true;
}



bool AWeaponBase::GetLookVectorHitLocation(FVector LookDirection, FHitResult & HitResult) const
{

	if (GetWorld()->GetFirstPlayerController() == nullptr) { HitResult = FHitResult(); return false; }

	FHitResult HitInfo;



	auto StartLocation = GetWorld()->GetFirstPlayerController()->PlayerCameraManager->GetCameraLocation();//The start location of the line trace 
	auto EndLocation = (StartLocation + CalcSpread()) + (LookDirection * WeaponRange); //The end location of the line trace

	if (GetWorld()->LineTraceSingleByChannel(HitInfo, StartLocation, EndLocation, ECC_Weapon, TraceParams))
	{
		HitResult = HitInfo;
		auto HitLocation = HitResult.Location;

		// Once we done the first line trace we return the impact point
		//The Second line trace starts from the character and the the endlocation is the impact point of the first line trace 
		//auto Start = GetWorld()->GetFirstPlayerController()->GetControlledPawn()->GetGetMesh()->GetSocketLocation("WeaponSocket");
		auto Start = WeaponMesh->GetSocketLocation(MuzzleSocketName);
		GetWorld()->LineTraceSingleByChannel(HitResult, Start, HitLocation, ECC_Weapon, TraceParams);
		//DrawDebugLine(GetWorld(), Start, HitLocation, FColor(255, 0, 0), true, 10.f);


		return true;
	}

	HitInfo = FHitResult();
	return false;
}

bool AWeaponBase::GetLookDirection(FVector2D ScreenLocation, FVector & LookDirection) const
{
	FVector CameraWorldLocation;//REMOVE LATER

	//Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value.
	return GetWorld()->GetFirstPlayerController()->DeprojectScreenPositionToWorld(ScreenLocation.X, ScreenLocation.Y, CameraWorldLocation, LookDirection);

}


void AWeaponBase::StartReload()
{
	

	bCanReload = false;//Stops the player from reloading again
	bCanFire = false;//Stops the player from shooting when reloading
	

	float AnimDuration = PlayWeaponAnimation(ReloadAnim);
	if (AnimDuration <= 0.0f)
	{
		AnimDuration = NoAnimReloadDuration;
	}

	GetWorldTimerManager().SetTimer(TimerHandle_StopReload, this, &AWeaponBase::StopSimulateReload, AnimDuration, false);

	GetWorldTimerManager().SetTimer(TimerHandle_ReloadWeapon, this, &AWeaponBase::ReloadWeapon, FMath::Max(0.1f, AnimDuration - 0.1f), false);

	if (GetPawnOwner() && GetPawnOwner()->IsLocallyControlled())
	{
		PlayWeaponSound(ReloadSound);
	}

}

void AWeaponBase::ReloadWeapon()
{


	int32 NeededAmmo = MaxAmmoPerClip - CurrentAmmoInClip;

	if (CurrentAmmoInGun >= NeededAmmo)
	{

		CurrentAmmoInClip = CurrentAmmoInClip + NeededAmmo;
		CurrentAmmoInGun = CurrentAmmoInGun - NeededAmmo;
	}
	else {

		if (CurrentAmmoInGun > 0)
		{

			CurrentAmmoInClip = CurrentAmmoInClip + CurrentAmmoInGun;
			CurrentAmmoInGun = 0;
		}
		else
		{
			//TODO -  Print to screen telling the player the Gun is empty
			//UE_LOG(LogTemp, Warning, TEXT("Ammo gone"))
		}
	}

	/*Once the reload is over allow the player to reload and fire the gun again*/
	bCanReload = true;
	bCanFire = true;
	GetWorldTimerManager().ClearTimer(TimerHandle_ReloadWeapon);
}

bool AWeaponBase::GetCanReload()
{
	return bCanReload;
}

void AWeaponBase::CheckIfPlayerCanReload()
{
	/*Checks to see if there is bullets in the gun to reload*/
	/*Doesnt play animation when the clip is full and check to if we can reload*/
	if (CurrentAmmoInGun <= 0 || CurrentAmmoInClip == MaxAmmoPerClip || !GetCanReload() || !bCanEquip)
	{
		return;
	}

	StartReload();
}


void AWeaponBase::StopSimulateReload()
{
	StopWeaponAnimation(ReloadAnim);
}





int32 AWeaponBase::GetCurrentAmmoInClip() const
{
	return CurrentAmmoInClip;
}

int32 AWeaponBase::GetCurrentAmmoInGun() const
{
	return CurrentAmmoInGun;
}

FVector AWeaponBase::CalcSpread() const
{

	//TODO - Maybe add the feature if the player is aiming less weapon spread
	if (GetPawnOwner()->GetIsAiming())
	{


	}
	//This gets a random number and stores it in a vector which then gets added to the Endtrace. 
	int32 RandomX = FMath::RandRange(-100, 100);
	int32 RandomY = FMath::RandRange(-100, 100);
	int32 RandomZ = FMath::RandRange(-100, 100);

	const FVector RandomVector = FVector(RandomX * WeaponSpread, RandomY * WeaponSpread, RandomZ * WeaponSpread);

	return RandomVector;
}

void AWeaponBase::Recoil()
{
	//TODO - Improve recoil by using lerp

	float Recoil = VerticalRecoilAmount * -1;
	GetWorld()->GetFirstPlayerController()->AddPitchInput(Recoil);
	GetWorld()->GetFirstPlayerController()->AddYawInput(HorizontalRecoilAmount);

}

void AWeaponBase::UseAmmo()
{
	CurrentAmmoInClip--;
}

void AWeaponBase::SpawnMuzzleEffect()
{
	FVector Location = WeaponMesh->GetSocketLocation(MuzzleSocketName);
	FRotator Rotation = WeaponMesh->GetSocketRotation(MuzzleSocketName);
	UGameplayStatics::SpawnEmitterAttached(ShotEffect, WeaponMesh, MuzzleSocketName, Location, Rotation, EAttachLocation::KeepWorldPosition, true);
	UGameplayStatics::SpawnSoundAttached(FireSound, WeaponMesh, MuzzleSocketName, Location, EAttachLocation::KeepWorldPosition, true, 1, 1, 0);
}

void AWeaponBase::SpawnTrailEffect(FVector& EndPoint)
{

	BSCount++;

	const FVector Origin = WeaponMesh->GetSocketLocation(MuzzleSocketName);
	FVector ShootDir = EndPoint - Origin;


	if (BSCount % 3 == 0)
	{
		if (TrailEffect)
		{
			ShootDir.Normalize();
			UGameplayStatics::SpawnEmitterAtLocation(this, TrailEffect, Origin, ShootDir.Rotation());
		}
	}

}

void AWeaponBase::SpawnImpactEffect(FHitResult& Hit)
{
	FVector Location = Hit.ImpactPoint;
	FRotator Rotation = Hit.ImpactPoint.Rotation();
	UGameplayStatics::SpawnEmitterAtLocation(GetWorld(), ImpactEffect, Location, Rotation, true);
	UGameplayStatics::PlaySoundAtLocation(GetWorld(), ImpactSound, Location, Rotation, 1, 1, 0);

}

void AWeaponBase::ChangeOwner(AActor * NewOwner)
{
	APlayerCharacter* Player = Cast<APlayerCharacter>(NewOwner);
	if (Player) {
		OwningPlayer = Player;
	}
	SetOwner(NewOwner);
}


void AWeaponBase::OnInteract(AActor* Caller) {
	APlayerCharacter* Player = Cast<APlayerCharacter>(Caller);
	if (Player)
	{
		Player->AddToInventory(this);
	}
}

void AWeaponBase::OnPlayerEnterPickupBox(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult & SweepResult)
{
	/*class APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	if (Player)
	{
	UE_LOG(LogTemp, Warning, TEXT("Hi"))
	}
	else
	{
	UE_LOG(LogTemp, Warning, TEXT("Not Working"))
	}*/
	if (bCanInteract)
	{
		OnInteract(OtherActor);
	}

}

void AWeaponBase::SetCanInteract(bool NewInteract)
{
	bCanInteract = NewInteract;
}

float AWeaponBase::PlayWeaponAnimation(UAnimMontage* Animation, float InPlayRate, FName StartSectionName)
{
	
		float Duration = 0.0f;
	if (GetPawnOwner())
	{
		if (Animation)
		{
			Duration = GetPawnOwner()->PlayAnimMontage(Animation, InPlayRate, StartSectionName);
		}
	}

	return Duration;
}

void AWeaponBase::StopWeaponAnimation(UAnimMontage* Animation)
{
	if (GetPawnOwner())
	{
		if (Animation)
		{
			GetPawnOwner()->StopAnimMontage(Animation);
		}
	}
}

UAudioComponent* AWeaponBase::PlayWeaponSound(USoundCue* SoundToPlay)
{
	
		UAudioComponent* AC = nullptr;
	if (SoundToPlay && GetPawnOwner())
	{
		AC = UGameplayStatics::SpawnSoundAttached(SoundToPlay, GetPawnOwner()->GetRootComponent());
	}

	return AC;
}

float AWeaponBase::GetEquipStartedTime() const
{
	return EquipStartedTime;
}


float AWeaponBase::GetEquipDuration() const
{
	return EquipDuration;
}


void AWeaponBase::OnEquip(bool bPlayAnimation)
{



	bCanEquip = false;
	bCanFire = false;
	

	if (bPlayAnimation)
	{
		float Duration = PlayWeaponAnimation(EquipAnim);
		if (Duration <= 0.0f)
		{
			// Failsafe in case animation is missing
			Duration = NoEquipAnimDuration;
		}
		EquipStartedTime = GetWorld()->TimeSeconds;
		EquipDuration = Duration;

		GetWorldTimerManager().SetTimer(EquipFinishedTimerHandle, this, &AWeaponBase::OnEquipFinished, Duration, false);
	}
	else
	{
		/* Immediately finish equipping */
		OnEquipFinished();
	}

	if (GetPawnOwner() && GetPawnOwner()->IsLocallyControlled())
	{
		PlayWeaponSound(EquipSound);
	}
}

void AWeaponBase::OnEquipFinished()
{
	
	bCanEquip = true;
	bCanFire = true;
	GetWorldTimerManager().ClearTimer(EquipFinishedTimerHandle);
	

}

bool AWeaponBase::IsEquipped() const
{
	return bIsEquipped;
}


