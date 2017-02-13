   // Copyright 

#include "GroupProject.h"
#include "EnemyController.h"
#include "AIMeleeCharacter.h"//Character
#include "AIShootingCharacter.h"
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

	Enemy = "Enemy";
	HeardNoiseLocation = "NoiseLocation";
	EnemyLastSeenLocation = "EnemyLastSeenLocation";
	CurrentPatrolPoint = 0;
}


void AEnemyController::Possess(APawn * PossessPawn)
{
	Super::Possess(PossessPawn);

	//Get Reference to Character

	AAIEnemyMaster* AICharacter = Cast<AAIEnemyMaster>(PossessPawn);

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

void AEnemyController::SetSeenEnemy(APawn * NewTarget)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsObject(Enemy, NewTarget);
	}
}

void AEnemyController::SetNoiseLocation(FVector Location)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsVector(HeardNoiseLocation,Location);
	}
}

void AEnemyController::SetEnemyLastSeebLocation(FVector Location)
{
	if (BlackboardComp)
	{
		BlackboardComp->SetValueAsVector(EnemyLastSeenLocation, Location);
	}
}

APawn* AEnemyController::GetCurrentTarget()
{
	APawn* CurrentTarget = Cast<APawn>(BlackboardComp->GetValueAsObject(PlayerKey));
	return CurrentTarget;
}
