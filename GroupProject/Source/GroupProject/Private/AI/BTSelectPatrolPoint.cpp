// Copyright 

#include "GroupProject.h"
#include "BTSelectPatrolPoint.h"
#include "AIPatrolPoint.h"
#include "EnemyController.h"
#include "BehaviorTree/BlackboardComponent.h"

EBTNodeResult::Type UBTSelectPatrolPoint::ExecuteTask(UBehaviorTreeComponent & OwnerComp, uint8 * NodeMemory)
{
	AEnemyController* AICon = Cast<AEnemyController>(OwnerComp.GetAIOwner());
	
	if (AICon)
	{
		//Get BB Comp
		UBlackboardComponent* BlackboardComp = AICon->GetBlackboardComp();

		AAIPatrolPoint* CurrentPoint = Cast<AAIPatrolPoint>(BlackboardComp->GetValueAsObject("LocationToGo"));

		//Creating array
		TArray<AActor*> AvailablePatrolPoints = AICon->GetPAtrolPoints();
		//Fails if we dont have any patrol points
		if (AvailablePatrolPoints.Num() == 0) {return EBTNodeResult::Failed;}

		AActor* NextPatrolPoint = nullptr;

		NextPatrolPoint = AvailablePatrolPoints[FMath::RandRange(0, AvailablePatrolPoints.Num() - 1)];
		if (NextPatrolPoint)
		{
			BlackboardComp->SetValueAsObject("WonderPointToGo", NextPatrolPoint);
			return EBTNodeResult::Succeeded;
		}
		
	}
	return EBTNodeResult::Failed;
}
