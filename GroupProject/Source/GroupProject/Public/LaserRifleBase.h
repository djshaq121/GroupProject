// Copyright 

#pragma once

#include "WeaponBase.h"
#include "LaserRifleBase.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API ALaserRifleBase : public AWeaponBase
{
	GENERATED_BODY()
	
public:

// Called every frame

	virtual void Tick(float DeltaTime) override;
	virtual void BeginPlay() override;

	virtual void DoFire();

	void FiringGun();

private:
	bool bIsCoolingDown = false;
	
	UPROPERTY(EditDefaultsOnly)
	float Heat = 0.f;
	UPROPERTY(EditDefaultsOnly)
	float HeatTheshold = 5.f;
	UPROPERTY(EditDefaultsOnly)
	float CoolDownTime = 1.5f;
	UPROPERTY(EditDefaultsOnly)
	float OverHeatTime = 2.5f;
	UPROPERTY(EditDefaultsOnly)
	float newHeat;
};
