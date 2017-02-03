   // Copyright 

#include "GroupProject.h"
#include "EnemyController.h"
#include "AIMeleeCharacter.h"//Character
#include "AIPatrolPoint.h"
#include "AIEnemyMaster.h"
#include "BehaviorTree/BehaviorTree.h"
#include "BehaviorTree/BehaviorTreeComponent.h"
#include "BehaviorTree/BlackboardComponent.h"
#include "BehaviorTree/Blackboard/BlackboardKeyAllTypes.h"



AEnemyController::AEnemyController()
{

	BehaviorComp = CreateDefaultSubobject<UBehaviorTreeComponent>(TEXT("BehaviorComp"));
	BlackboardComp = CreateDefaultSubobject<UBlackboardComponent>(TEXT("BlackboardComp"));

	//Initialize Blackboard Keys
	PlayerKey = "Target";
	LocationToGoKey = "LocationToGo";
	CurrentPatrolPoint = 0;
}

void AEnemyController::SetPlayerCaught(APawn * Pawn)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsObject(PlayerKey, Pawn);
	}
}

void AEnemyController::Possess(APawn * Pawn)
{
	Super::Possess(Pawn);

	//Get Reference to Character

	AAIEnemyMaster* AICharacter = Cast<AAIEnemyMaster>(Pawn);

	if (AICharacter)
	{
		if (AICharacter->BehaviorTree->BlackboardAsset)
		{
			BlackboardComp->InitializeBlackboard(*(AICharacter->BehaviorTree->BlackboardAsset));
		}

		//Populate Patrol Point Array
		UGameplayStatics::GetAllActorsOfClass(GetWorld(), AAIPatrolPoint::StaticClass(), PatrolPoints);
		BehaviorComp->StartTree(*AICharacter->BehaviorTree);
	}
}


void AEnemyController::SetTargetEnemy(APawn * NewTarget)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsObject(PlayerKey, NewTarget);
	}
}

APawn* AEnemyController::GetCurrentTarget()
{
	APawn* CurrentTarget = Cast<APawn>(BlackboardComp->GetValueAsObject(PlayerKey));
	return CurrentTarget;
}
