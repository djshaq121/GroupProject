// Copyright 

#include "GroupProject.h"
#include "LaserRifleBase.h"



void ALaserRifleBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	UE_LOG(LogTemp, Warning, TEXT("Heat Level: %f"), CurrentHeat)
	
	//CurrentHeat = FMath::FInterpTo(CurrentHeat, HeatThreshold, DeltaTime, 3.f);
	if (bIsCoolingDown)
	{
		CurrentHeat -= CoolDownTime * DeltaTime;
		if (CurrentHeat <= 0.f) {
			bIsCoolingDown = false; 
			bCanFire = true; 
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


	//GetWorld()->LineTraceSingleByChannel(HitResult, Start, End, ECC_Weapon, TraceParams);


	UseAmmo();
	FiringGun();
	//UE_LOG(LogTemp, Warning, TEXT("CurrentAmmo in clip %d"), CurrentAmmoInClip)
	
	if (GetSightRayHitLocation(Hit))
	{
		auto HitLocation = Hit.Location;
		//UE_LOG(LogTemp, Warning, TEXT("Hit Direction: %s "), *HitLocation.ToString());

	}
	if (Hit.GetActor())
	{
		
		//Calls DealDamage passing the actor we hit
		DealDamage(Hit);
		//SpawnImpactEffect
	}
}