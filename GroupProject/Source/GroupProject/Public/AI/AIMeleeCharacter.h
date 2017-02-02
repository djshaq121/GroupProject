// Copyright 

#pragma once

#include "AIEnemyMaster.h"
#include "AIMeleeCharacter.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AAIMeleeCharacter : public AAIEnemyMaster
{
	GENERATED_BODY()

		UPROPERTY(VisibleAnywhere, Category = "AI")
		class UPawnSensingComponent* PawnSensingComp;

		/* Last time the player was spotted */
		float LastSeenTime;

		UPROPERTY(EditDefaultsOnly, Category = "AI")
			float SenseTimeOut;

	/* Last time the player was heard */
		float LastHeardTime;

		/* Resets after sense time-out to avoid unnecessary clearing of target each tick */
		bool bSensedTarget;

public:

	/* Last time we attacked something */
	float LastMeleeAttackTime;

	AAIMeleeCharacter();

	void Tick(float DeltaSeconds);

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	UFUNCTION()
	void OnPlayerCaught(APawn * Pawn);

protected:

	UFUNCTION()
		void OnSeePlayer(APawn* Pawn);



	UAudioComponent* PlayCharacterSound(USoundCue* CueToPlay);
	UPROPERTY(EditDefaultsOnly, Category = "Sound")
		USoundCue* SoundAttackMelee;

	/* Timer handle to manage continous melee attacks while in range of a player */
	FTimerHandle TimerHandle_MeleeAttack;

	/* Minimum time between melee attacks */
	float MeleeStrikeCooldown;

	UFUNCTION(Reliable, NetMulticast)
		void SimulateMeleeStrike();

	void SimulateMeleeStrike_Implementation();

	UPROPERTY(EditDefaultsOnly, Category = "Attacking")
		TSubclassOf<UDamageType> PunchDamageType;

	UPROPERTY(EditDefaultsOnly, Category = "Attacking")
		float MeleeDamage;

	UPROPERTY(EditDefaultsOnly, Category = "Attacking")
		UAnimMontage* MeleeAnimMontage;

	void OnRetriggerMeleeStrike();

	/* Deal damage to the Actor that was hit by the punch animation */
	UFUNCTION(BlueprintCallable, Category = "Attacking")
		void PerformMeleeStrike(AActor* HitActor);

	UFUNCTION()
		void OnMeleeCompBeginOverlap(class UPrimitiveComponent* OverlappedComponent, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & SweepResult);

	UPROPERTY(VisibleAnywhere, Category = "Attacking")
		UCapsuleComponent* MeleeCollisionComp;

	UFUNCTION(BlueprintCallable, Category = "AI")
	int GetCurrentHealth() const;

	void SetRagdollPhysics();

	void OnDeath();

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser);

private:
	

	
};
