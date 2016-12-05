// Copyright 

#include "GroupProject.h"
#include "LaserRifleBase.h"



void ALaserRifleBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	//UE_LOG(LogTemp, Warning, TEXT("Heat Level: %f"), newHeat);
	if (bIsCoolingDown)
	{
		Heat -= CoolDownTime * DeltaTime;
		if (Heat <= 0.f) { bIsCoolingDown = false; bCanFire = true; }
	}
	
}

void ALaserRifleBase::BeginPlay()
{
	Super::BeginPlay();

}

void ALaserRifleBase::FiringGun()
{
	Heat += OverHeatTime * GetWorld()->GetDeltaSeconds();
	newHeat = FMath::Clamp(Heat, 0.f, HeatTheshold);
	
	if (newHeat >= HeatTheshold) {//Check to see if the heat of the gun is larger than the threshold
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


	CurrentAmmoInClip--;
	FiringGun();
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