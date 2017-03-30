// Copyright 

#include "GroupProject.h"
#include "LaserRifleBase.h"



void ALaserRifleBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	
	if (!bIsFiring || bIsCoolingDown)//Checks to see if the player is not shooting or the gun is cooldown
	{
		CurrentHeat -= CoolDownTime * DeltaTime; 
		if (CurrentHeat <= 0.f) { //Sets the weapon heat to zero if it reaches 0 or below 
			bIsCoolingDown = false; 
			SetCanFire(true);//Once the gun is cooled down allow the player to fire again
			CurrentHeat = 0;
		}
	}
	
	
}

bool ALaserRifleBase::GetIsOverHeated() const
{
	return bIsCoolingDown;
}

void ALaserRifleBase::BeginPlay()
{
	Super::BeginPlay();

}

void ALaserRifleBase::FiringGun()
{

	auto Time = GetWorld()->GetDeltaSeconds();
	
	//Increase heat when gun is fired
	CurrentHeat += OverHeatTime * Time;
	 CurrentHeat = FMath::Clamp(CurrentHeat, 0.f, HeatThreshold);
	
	
	if (CurrentHeat >= HeatThreshold) {//Check to see if the heat of the gun is larger than the threshold
		bIsCoolingDown = true;  //If its true than, guns goes on cool down
		SetCanFire(false);//Stop the player from firing again
		if (OverHeatSound)
		{
			UGameplayStatics::PlaySoundAttached(OverHeatSound, WeaponMesh, MuzzleSocketName, WeaponMesh->GetSocketLocation(MuzzleSocketName), EAttachLocation::KeepWorldPosition, true, 1, 1, 0);
		}
		
	};
}

void ALaserRifleBase::DoFire()
{
	

		SpawnMuzzleEffect();
		FHitResult Hit = FHitResult();
		FVector Start;

		GetCurrentHeat();
		


		UseAmmo();
		FiringGun();
		

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
			
		}
	
}

float ALaserRifleBase::GetCurrentHeat() const
{
	float CHeat = CurrentHeat / HeatThreshold;

	return CHeat;

}