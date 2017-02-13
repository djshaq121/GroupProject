// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "AIEnemyMaster.generated.h"

UCLASS()
class GROUPPROJECT_API AAIEnemyMaster : public ACharacter
{
	GENERATED_BODY()



public:
	

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser);

	UPROPERTY(EditAnywhere, Category = "AI")
		class UBehaviorTree* BehaviorTree;

protected:

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health")
		int32 CurrentHealth;

	UFUNCTION(BlueprintCallable, Category = "AI")
		int GetCurrentHealth() const;

	void SetRagdollPhysics();

	virtual void OnDeath();

	/* Last time the player was spotted */
	float LastSeenTime;

	UPROPERTY(EditDefaultsOnly, Category = "AI")
	float SenseTimeOut;

	/* Last time the player was heard */
	float LastHeardTime;

	/* Resets after sense time-out to avoid unnecessary clearing of target each tick */
	bool bSensedTarget;

	

private:


	UPROPERTY(VisibleAnywhere, Category = "Setup")
	int32 CurrentArmor = 0;


	bool bIsDead = false;
	
	bool IsAggroed;

	

};
