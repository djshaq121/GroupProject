// Copyright 

#include "GroupProject.h"
#include "AIPatrolController.h"
#include "AIPatrol.h"
#include "AIPatrolPoint.h"
#include "BehaviorTree/BlackboardComponent.h"
#include "BehaviorTree/BehaviorTreeComponent.h"
#include "BehaviorTree/BehaviorTree.h"

AAIPatrolController::AAIPatrolController()
{
	//Initialize Blackboard and BehaviorTree

	BehaviorComp = CreateDefaultSubobject<UBehaviorTreeComponent>(TEXT("BehaviorComp"));
	BlackboardComp = CreateDefaultSubobject<UBlackboardComponent>(TEXT("BlackboardComp"));

	//Initialize Blackboard Keys
	PlayerKey = "Target";
	PlayerKeyID = "Player";
	LocationToGoKey = "LocationToGo";
	CurrentPatrolPoint = 0;
}

void AAIPatrolController::SetPlayerCaught(APawn * Pawn)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsObject(PlayerKey, Pawn);
	}
}


void AAIPatrolController::Possess(APawn * Pawn)
{
	Super::Possess(Pawn);

	//Get Reference to Character

	AAIPatrol* AICharacter = Cast<AAIPatrol>(Pawn);

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


