// Copyright 

#pragma once

#include "PickUpBase.h"
#include "HealthPickUp.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AHealthPickUp : public APickUpBase
{
	GENERATED_BODY()
	
public:

	AHealthPickUp();

	UFUNCTION()//Actor is gonna be us - We need to type check it so only the player can pick it up
		virtual void OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult);


private:

	UPROPERTY(EditDefaultsOnly, Category = "Health & Armor")
		float HealthAmount = 25.f;
	
	
};
