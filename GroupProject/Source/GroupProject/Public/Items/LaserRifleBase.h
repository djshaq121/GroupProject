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

	UFUNCTION(BlueprintCallable, Category = "UI")
	float GetCurrentHeat() const;

private:
	bool bIsCoolingDown = false;
	UPROPERTY(EditDefaultsOnly)
	float CurrentHeat = 0.f;
	UPROPERTY(EditDefaultsOnly)
	float HeatThreshold = 5.f;
	UPROPERTY(EditDefaultsOnly)
	float CoolDownTime = 1.5f;
	UPROPERTY(EditDefaultsOnly)
	float OverHeatTime = 2.5f;

	//We Created this because we cant use bCanFire, it will create run time errors
	bool bLRCanFire = true;
	
};
