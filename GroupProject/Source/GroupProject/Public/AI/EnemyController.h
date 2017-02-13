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

	TArray<AActor*> PatrolPoints;

	virtual void Possess(APawn* Pawn) override;



public:

	AEnemyController();


	void SetTargetEnemy(APawn* NewTarget);

	void SetSeenEnemy(APawn * NewTarget);

	void SetNoiseLocation(FVector Location);

	void SetEnemyLastSeebLocation(FVector Location);

	APawn * GetCurrentTarget();

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName PlayerKey;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName Enemy;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName HeardNoiseLocation;

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName EnemyLastSeenLocation;



	int32 CurrentPatrolPoint = 0;


	FORCEINLINE UBlackboardComponent* GetBlackboardComp() const { return BlackboardComp; }
	FORCEINLINE TArray<AActor*> GetPAtrolPoints() const { return PatrolPoints; }
	
	
};
