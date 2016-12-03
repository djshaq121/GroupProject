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

	
	CurrentAmmoInClip = StartAmmoClip;
	
	
}

// Called when the game starts or when spawned
void AWeaponBase::BeginPlay()
{
	Super::BeginPlay();
	if (bCanInteract)
	{
		CollisonSphere->OnComponentBeginOverlap.AddDynamic(this, &AWeaponBase::OnPlayerEnterPickupBox);
	}

	//CurrentAmmoInClip = StartAmmoClip;
	//CurrentMaxAmmoInGun = StartMaxAmmo;

}

/*PickUp*/

// Called every frame
void AWeaponBase::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );
	
}



void  AWeaponBase::DealDamage(const FHitResult& Hit)
{
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
		Hit.GetActor()->TakeDamage(DealtDamage, DamageEvent, GetPawnOwner()->GetController(), this);
		//Had a problem were if the player look down or up they could shoot themselves. Fixed by using custom preset on player
	}
}

/*The method that is called in weapon class*/
void  AWeaponBase::StartFire()
{
	
	if (CurrentAmmoInClip > 0)
	{
		DoFire();
		//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo %d"), CurrentAmmoInClip)
		float TimerDelay = FireRate > 0 ? 1 / (FireRate*0.01667) : FApp::GetDeltaTime();

		auto World = GetWorld();
		if (World) {
			//This what makes the doFire loop when its held down
			//This calls the &AWeaponBase::StartFire and loops because we set it to true ,
			if (!FireRateHandle.IsValid())
			{
				World->GetTimerManager().SetTimer(FireRateHandle, this, &AWeaponBase::StartFire, TimerDelay, true);//This will loop the startfire because we set it to true

			}
		}
		else {
			StopFire();
		}
	}
	
}
void  AWeaponBase::StopFire()
{
	UE_LOG(LogTemp, Warning, TEXT("Stop Fire"));
	GetWorld()->GetTimerManager().ClearTimer(FireRateHandle);
	FireRateHandle.Invalidate();
}

void  AWeaponBase::DoFire()
{
	FHitResult Hit = FHitResult();
	FVector Start;

	


		//GetWorld()->LineTraceSingleByChannel(HitResult, Start, End, ECC_Weapon, TraceParams);


	CurrentAmmoInClip--;
	//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo in clip %d"), CurrentAmmoInClip)

	if (GetSightRayHitLocation(Hit))
	{
			auto HitLocation = Hit.Location;
			//UE_LOG(LogTemp, Warning, TEXT("Hit Direction: %s "), *HitLocation.ToString());

	}
	if (Hit.GetActor())
	{
		UE_LOG(LogTemp, Warning, TEXT("Actor hit: %s "), *Hit.GetActor()->GetName());
		//Calls DealDamage passing the actor we hit
		DealDamage(Hit);
		//SpawnImpactEffect
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
	auto EndLocation = StartLocation + (LookDirection * LineTraceRange); //The end location of the line trace

	if (GetWorld()->LineTraceSingleByChannel(HitInfo, StartLocation, EndLocation, ECC_Weapon, TraceParams))
	{
		HitResult = HitInfo;
		auto HitLocation = HitResult.Location;

		// Once we done the first line trace we return the impact point
		//The Second line trace starts from the character and the the endlocation is the impact point of the first line trace 
		//auto Start = GetWorld()->GetFirstPlayerController()->GetControlledPawn()->GetGetMesh()->GetSocketLocation("WeaponSocket");
		auto Start = WeaponMesh->GetSocketLocation(MuzzleSocketName);
		GetWorld()->LineTraceSingleByChannel(HitResult, Start, HitLocation, ECC_Weapon, TraceParams);
		
		DrawDebugLine(GetWorld(), Start, HitLocation, FColor(0, 0, 255), true);
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

class APlayerCharacter* AWeaponBase::GetPawnOwner() const
{
	auto playerpawn = GetWorld()->GetFirstPlayerController()->GetPawn();
	if (!playerpawn) { return nullptr; }

	return Cast<APlayerCharacter>(playerpawn);
}