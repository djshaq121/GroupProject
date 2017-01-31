// Copyright 

#include "GroupProject.h"
#include "LaserRifleBase.h"



void ALaserRifleBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	//UE_LOG(LogTemp, Warning, TEXT("Heat Level: %f"), CurrentHeat)
	if (!bIsFiring || bIsCoolingDown)//Checks to see if the player is not shooting or the gun is cooldown
	{
		CurrentHeat -= CoolDownTime * DeltaTime; 
		if (CurrentHeat <= 0.f) { //Sets the weapon heat to zero if it reaches 0 or below 
			bIsCoolingDown = false; 
			bCanFire = true; //Allow the player to shoot one the gun is not on cooldown
			CurrentHeat = 0;
		}
	}
	
	
}

void ALaserRifleBase::BeginPlay()
{
	Super::BeginPlay();

}

void ALaserRifleBase::FiringGun()
{

	auto Time = GetWorld()->GetDeltaSeconds();
	
	CurrentHeat += OverHeatTime * Time;
	//Heat = FMath::FInterpTo(0, HeatThreshold, Time, 30.f);
	 CurrentHeat = FMath::Clamp(CurrentHeat, 0.f, HeatThreshold);
	
	
	if (CurrentHeat >= HeatThreshold) {//Check to see if the heat of the gun is larger than the threshold
		bIsCoolingDown = true;  //If its true than, guns goes on cool down
		bCanFire = false; //Stop the player from firing
		UE_LOG(LogTemp, Warning, TEXT("OnCoolDown"));
	};
}

void ALaserRifleBase::DoFire()
{
	FHitResult Hit = FHitResult();
	FVector Start;

	GetCurrentHeat();
	//GetWorld()->LineTraceSingleByChannel(HitResult, Start, End, ECC_Weapon, TraceParams);


	UseAmmo();
	FiringGun();
	//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo in clip %d"), CurrentAmmoInClip)
	
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
		
		//Calls DealDamage passing the actor we hit
		DealDamage(Hit);
		//SpawnImpactEffect
	}
}

float ALaserRifleBase::GetCurrentHeat() const
{
	float CHeat = CurrentHeat / HeatThreshold;

	return CHeat;

	UE_LOG(LogTemp, Warning, TEXT("Heat Level: %f"), CHeat)
}