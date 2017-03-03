// Copyright 

#pragma once

#include "PickUpBase.h"
#include "ArmorPickUp.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AArmorPickUp : public APickUpBase
{
	GENERATED_BODY()

public:

	AArmorPickUp();

	UFUNCTION()

	//Actor is gonna be us - We need to type check it so only the player can pick it up
		virtual void OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult);
	

private:

	UPROPERTY(EditDefaultsOnly, Category = "Health & Armor")
		float ArmorAmount = 25.f;


};