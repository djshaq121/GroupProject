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
	
public:

	AAIMeleeCharacter();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

protected:

	UFUNCTION(BlueprintCallable, Category = "AI")
	int GetCurrentHealth() const;

	void SetRagdollPhysics();

	void OnDeath();

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser);

private:
	

	
};
