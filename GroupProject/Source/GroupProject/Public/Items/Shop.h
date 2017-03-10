// Copyright LostGods

#pragma once

#include "Items/InteractableActor.h"
#include "Shop.generated.h"

/**
 * 
 */

DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnShopOpen);

UCLASS()
class GROUPPROJECT_API AShop : public AInteractableActor
{
	GENERATED_BODY()
	
public:
	UPROPERTY(BlueprintAssignable)
	FOnShopOpen ShopToggle;
	virtual void OnInteract_Implementation(AActor* Caller) override;
	
	
};
