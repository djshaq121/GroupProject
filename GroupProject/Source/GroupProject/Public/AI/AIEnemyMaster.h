// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "AIEnemyMaster.generated.h"

UENUM(BlueprintType)
enum class EAIState : uint8
{
	Passive UMETA(DisplayName = "Passive"),
	Aggro UMETA(DisplayName = "Aggro"),
	Combat UMETA(DisplayName = "Combat")

};

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

	virtual void DetermineAiState();

	int32 GetGoldReward() const;

	int32 GetScoreReward() const;

	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Interaction")
	void OnInteract(AActor* Caller);

	virtual void OnInteract_Implementation(AActor* Caller);

	
 void SpawnItemDrop(FVector Location, FRotator Rotation);
	

protected:

	

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

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

	UFUNCTION(BlueprintCallable, Category = "AI")
	bool GetIsDead() const;

	void SetIsDead(bool NewState);

	UPROPERTY(EditDefaultsOnly)
	int32 GoldReward;

	UPROPERTY(EditDefaultsOnly)
	int32 Score;

	UPROPERTY(EditDefaultsOnly, Category = "Items")
	TArray<TSubclassOf<class APickUpBase> > ItemDrops;
	
	UPROPERTY(EditDefaultsOnly, Category = "Items")
		float ItemProbability = 0.f;
private:



	bool bIsDead = false;
	
	bool IsAggroed;

	

};
