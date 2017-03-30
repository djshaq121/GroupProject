// Copyright 

#pragma once

#include "AIController.h"
#include "EnemyController.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AEnemyController : public AAIController
{
	GENERATED_BODY()
	
		/*Behavior Tree Component*/
		UBehaviorTreeComponent* BehaviorComp;

	/*Blackboard Component*/
	UBlackboardComponent* BlackboardComp;

	/*Blackboard Keys*/
	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName LocationToGoKey;

	//List of points to travel to
	TArray<AActor*> PatrolPoints;

	
	virtual void Possess(APawn* Pawn) override;



public:
	UFUNCTION(BlueprintCallable, Category = "Behavior")
	void EnemyIsVisible();

	virtual void UnPossess() override;

	AEnemyController();

	//Enemy to chase
	void SetTargetEnemy(APawn* NewTarget);

	//Enemy seen
	void SetSeenEnemy(APawn * NewTarget);

	//Location to travel to
	void SetNoiseLocation(FVector Location);

	void SetEnemyLastSeenLocation(FVector Location);

	void SetEnemyVisible(bool IsVisble);

	APawn * GetCurrentTarget();

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName PlayerKey;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName Enemy;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName HeardNoiseLocation;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName EnemyLastSeenLocation;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName IsEnemyVisible;

	int32 CurrentPatrolPoint = 0;


	FORCEINLINE UBlackboardComponent* GetBlackboardComp() const { return BlackboardComp; }
	FORCEINLINE TArray<AActor*> GetPAtrolPoints() const { return PatrolPoints; }
	
	
};
