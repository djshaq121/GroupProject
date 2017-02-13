// Copyright 

#pragma once

#include "AI/AIEnemyMaster.h"
#include "AIShootingCharacter.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AAIShootingCharacter : public AAIEnemyMaster
{
	GENERATED_BODY()
	
public:
	AAIShootingCharacter();

	void Tick(float DeltaSeconds);

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	//Pawn senseing comp that allows the AI to see and hear
	UPROPERTY(VisibleAnywhere, Category = "AI")
	class UPawnSensingComponent* PawnSensingComp;

	

protected:


private:
	UFUNCTION()
		void OnSeePlayer(APawn* PawnInstigator);
	UFUNCTION()
		void OnHearNoise(APawn* PawnInstigator, const FVector & Location, float Volume);
	
};