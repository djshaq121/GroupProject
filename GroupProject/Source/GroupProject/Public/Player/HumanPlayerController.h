// Copyright 

#pragma once

#include "PlayerCharacter.h"
#include "GameFramework/PlayerController.h"
#include "DeathWidget.h"
#include "HumanPlayerController.generated.h"

/**
 * 
 */



UCLASS()
class GROUPPROJECT_API AHumanPlayerController : public APlayerController
{
	GENERATED_BODY()

public:

	void AimTowardsCrosshair();

	APlayerCharacter* GetControlledPlayer() const;


	//Called every frame
	virtual void Tick(float DeltaSeconds) override;

protected:
	UFUNCTION()//Needs the ufunction or it will run an ensure expection 
		void OnPossesPlayerDeath();
	
private:

	

	void SetPawn(APawn * InPawn);

	virtual void BeginPlay() override;



	
};
