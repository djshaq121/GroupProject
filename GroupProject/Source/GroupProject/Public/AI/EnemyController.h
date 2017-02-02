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

	UPROPERTY(EditDefaultsOnly, Category = AI)
		FName PlayerKey;

	TArray<AActor*> PatrolPoints;

	virtual void Possess(APawn* Pawn) override;



public:

	AEnemyController();

	virtual void Tick(float DeltaSeconds) override;

	//
	void SetTargetEnemy(APawn* NewTarget);

	APawn * GetCurrentTarget();

	UPROPERTY(EditDefaultsOnly, Category = AI)
	FName PlayerKeyID;

	void SetPlayerCaught(APawn* Pawn);

	int32 CurrentPatrolPoint = 0;

	//void SetPlayerCaught(APawn* Pawn);
	/*Getter Functions*/

	FORCEINLINE UBlackboardComponent* GetBlackboardComp() const { return BlackboardComp; }
	FORCEINLINE TArray<AActor*> GetPAtrolPoints() const { return PatrolPoints; }
	
	
};
