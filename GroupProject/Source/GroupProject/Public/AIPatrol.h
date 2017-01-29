// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "AIPatrol.generated.h"


UCLASS()
class GROUPPROJECT_API AAIPatrol : public ACharacter
{
	GENERATED_BODY()
		/* Last time we attacked something */
		float LastMeleeAttackTime;

protected:
	UPROPERTY(VisibleAnywhere, Category = "Attacking")
		UCapsuleComponent* MeleeCollisionComp;

	UPROPERTY(EditDefaultsOnly, Category = "Attacking")
		TSubclassOf<UDamageType> PunchDamageType;
	UPROPERTY(EditDefaultsOnly, Category = "Attacking")
		float MeleeDamage;

	void SetRagdollPhysics();
	virtual void OnDeath(float KillingDamage, FDamageEvent const& DamageEvent, APawn* PawnInstigator, AActor* DamageCauser);
	/* Deal damage to the Actor that was hit by the punch animation */
	UFUNCTION(BlueprintCallable, Category = "Attacking")
		void PerformMeleeStrike(AActor* HitActor);
public:
	// Sets default values for this character's properties
	AAIPatrol();
	float theTime;

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* InputComponent) override;
	// Called every frame

	//FPlayerDelegate OnDeath;

	//Make an IsDead property - So it can be caled in blueprint
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Setup")
		bool bIsDead = false;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Setup")
		bool bIsAiming = false;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser) override;

	UPROPERTY(EditAnywhere, Category = AI)
		class UBehaviorTree* BehaviorTree;

	UPROPERTY(VisibleAnywhere, Category = AI)
		class UPawnSensingComponent* PawnSensingComp;
	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
		int GetCurrentHealth() const;

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
		int GetCurrentArmor() const;

private:

	FTimerHandle UnusedHandle;

	UFUNCTION()
		void OnPlayerCaught(APawn* Pawn);

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
		int32 CurrentHealth;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumArmor = 0;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
		int32 CurrentArmor;

};
