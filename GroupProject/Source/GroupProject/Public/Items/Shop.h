// Copyright LostGods

#pragma once

#include "Items/InteractableActor.h"
#include "Shop.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AShop : public AInteractableActor
{
	GENERATED_BODY()
	
public:
	virtual void OnInteract_Implementation(AActor* Caller) override;
	
	
};
