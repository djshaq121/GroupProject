// Copyright 

#pragma once

#include "GameFramework/PlayerController.h"
#include "CharacterController.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API ACharacterController : public APlayerController
{
	GENERATED_BODY()


public:
		//The interactable the player is currently looking at is stored here to be displayed on screen
		UPROPERTY(BlueprintReadWrite, VisibleAnywhere)
		class AInteractableActor* CurrentInteractable;
	
};
