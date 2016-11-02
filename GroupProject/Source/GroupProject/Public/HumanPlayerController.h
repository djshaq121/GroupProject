// Copyright 

#pragma once

#include "PlayerCharacter.h"
#include "GameFramework/PlayerController.h"
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

protected:
	UFUNCTION()//Needs the ufunction or it will run an ensure expection 
		void OnPossesPlayerDeath();
	
private:

	void SetPawn(APawn * InPawn);

	virtual void BeginPlay() override;

	//Called every frame
	virtual void Tick(float DeltaSeconds) override;

	bool GetSightRayHitLocation(FVector& HitLocation) const;

	bool GetLookVectorHitLocation(FVector LookDirection, FVector& HitLocation) const;

	bool GetLookDirection(FVector2D ScreenLocation, FVector& LookDirection) const;

	//The position of the crosshair on screen 
	UPROPERTY(EditDefaultsOnly)
		float CrossHairXLocation = 0.5;

	UPROPERTY(EditDefaultsOnly)
		float CrossHairYLocation = 0.5;

	UPROPERTY(EditDefaultsOnly)
		float LineTraceRange = 5000.f;
};
