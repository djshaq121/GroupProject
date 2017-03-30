// Copyright 

#pragma once

#include "AI/AIEnemyMaster.h"
#include "AIShootingCharacter.generated.h"

/**
 * 
 */
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FAIOnDeathRequest);

class APlayerCharacter;

UCLASS()
class GROUPPROJECT_API AAIShootingCharacter : public AAIEnemyMaster
{
	GENERATED_BODY()
	
public:

	UPROPERTY(BlueprintAssignable)
	FAIOnDeathRequest AIOnDeathRequest;

	AAIShootingCharacter();

	void Tick(float DeltaSeconds);

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	//Pawn senseing comp that allows the AI to see and hear
	UPROPERTY(VisibleAnywhere, Category = "AI")
	class UPawnSensingComponent* PawnSensingComp;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser);

	void SetState(EAIState NewStates);

	UFUNCTION(BlueprintCallable, Category = "AI")
	bool GetIsAiming() const;

	
	UFUNCTION(BlueprintCallable, Category = "AI")
	void SetIsAiming(bool Aiming);

	FTimerHandle AimingTimeHandle;
	
	virtual void DetermineAiState();

protected:
	


private:
	/*Muzzle Effects*/
	UPROPERTY(EditDefaultsOnly)
	UParticleSystem* ShotEffect;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	FName WeaponSocketName;

	UFUNCTION()//If the enemy sees the player
		void OnSeePlayer(APawn* PawnInstigator);
	UFUNCTION()//if the enemy hears a noise
		void OnHearNoise(APawn* PawnInstigator, const FVector & Location, float Volume);

	EAIState States;

	bool bIsAiming = false;

	bool bIsEnemyVisible = false;
	
};
