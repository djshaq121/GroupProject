// Copyright 

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "WeaponBase.h"


// Sets default values
AWeaponBase::AWeaponBase()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	CollisonSphere = CreateDefaultSubobject<USphereComponent>(TEXT("CollisonSphere"));
	RootComponent = CollisonSphere;
	WeaponMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("GunMesh"));
	WeaponMesh->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);

	TraceParams = FCollisionQueryParams(FName(TEXT("Projectile Trace'")), true, this);

	


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
void AWeaponBase::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );
	
}

class APlayerCharacter* AWeaponBase::GetPawnOwner() const
{
	auto playerpawn = GetWorld()->GetFirstPlayerController()->GetPawn();
	if (!playerpawn) { return nullptr; }

	return Cast<APlayerCharacter>(playerpawn);
}

void AWeaponBase::Reload()
{

	int32 NeededAmmo = MaxAmmoPerClip - CurrentAmmoInClip;

	if (CurrentAmmoInGun >= NeededAmmo)
	{
		
		CurrentAmmoInClip = CurrentAmmoInClip + NeededAmmo;
		CurrentAmmoInGun = CurrentAmmoInGun - NeededAmmo;
	}
	else {

		if(CurrentAmmoInGun > 0)
		{
			
			CurrentAmmoInClip = CurrentAmmoInClip + CurrentAmmoInGun;
			CurrentAmmoInGun = 0;
		}
		else
		{
			//TODO -  Print to screen telling the player the Gun is empty
			UE_LOG(LogTemp, Warning, TEXT("Ammo gone"))
		}
	}
	

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

/*The method that is called in weapon class*/
void  AWeaponBase::StartFire()
{
	if (GetPawnOwner() != nullptr)//Stops the game from crashing when the player shoots and dies at the same time  
	{
		if (CurrentAmmoInClip > 0 && bCanFire)
		{
			SpawnMuzzleEffect();
			bIsFiring = true;
			DoFire();
			//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo %d"), CurrentAmmoInClip)
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
				//UE_LOG(LogTemp, Warning, TEXT("Out of ammo"));
				StopFire();

			}
		}
		//This reloads when the ammo reaches zero
		//if (CurrentAmmoInClip <= 0) { Reload(); }
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
	FHitResult Hit = FHitResult();
	FVector Start;


	UseAmmo();
	//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo in clip %d"), CurrentAmmoInClip)

	if (GetSightRayHitLocation(Hit))
	{
			auto HitLocation = Hit.Location;
			//Checks if we hit something
			if (Hit.bBlockingHit){	

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
	auto EndLocation = StartLocation + (LookDirection * WeaponRange); //The end location of the line trace

	if (GetWorld()->LineTraceSingleByChannel(HitInfo, StartLocation, EndLocation, ECC_Weapon, TraceParams))
	{
		HitResult = HitInfo;
		auto HitLocation = HitResult.Location;

		// Once we done the first line trace we return the impact point
		//The Second line trace starts from the character and the the endlocation is the impact point of the first line trace 
		//auto Start = GetWorld()->GetFirstPlayerController()->GetControlledPawn()->GetGetMesh()->GetSocketLocation("WeaponSocket");
		auto Start = WeaponMesh->GetSocketLocation(MuzzleSocketName);
		GetWorld()->LineTraceSingleByChannel(HitResult, Start, HitLocation, ECC_Weapon, TraceParams);
		
		
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

//void AWeaponBase::GetAmmo(int32 & Current, int32 & Max)
//{
//	Current = CurrentAmmoInClip;
//	Max = CurrentAmmoInGun;
//}

int32 AWeaponBase::GetCurrentAmmoInClip() const
{
	return CurrentAmmoInClip;
}

int32 AWeaponBase::GetCurrentAmmoInGun() const
{
	return CurrentAmmoInGun;
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
	UGameplayStatics::PlaySoundAttached(FireSound, WeaponMesh, MuzzleSocketName, Location, EAttachLocation::KeepWorldPosition, true, 1, 1, 0);
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
	UGameplayStatics::SpawnEmitterAtLocation(GetWorld(), ImpactEffect, Location, Rotation,true);
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

