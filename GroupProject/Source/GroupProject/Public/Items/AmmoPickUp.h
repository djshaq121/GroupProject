// Copyright LostGods

#pragma once

#include "Items/PickUpBase.h"
#include "GroupProject.h"
#include "AmmoPickUp.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AAmmoPickUp : public APickUpBase
{
	GENERATED_BODY()
	
public:
	virtual void OnInteract_Implementation(AActor* Caller);

	virtual void OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult);

private:
	UPROPERTY(BlueprintReadWrite, meta = (AllowPrivateAccess = "true"), Category = Hack)
	FPlayerInventory Inventory;

	UPROPERTY(EditDefaultsOnly)
	int32 AmmoAmount;
	UPROPERTY(EditDefaultsOnly)
	EAmmoType AmmoType;
	
};
