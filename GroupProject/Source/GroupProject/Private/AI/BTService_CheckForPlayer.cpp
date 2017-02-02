// Copyright 

#include "GroupProject.h"
#include "BTService_CheckForPlayer.h"
#include "AIEnemyMaster.h"
#include "BehaviorTree/BehaviorTree.h"
#include "BehaviorTree/BehaviorTreeComponent.h"
#include "BehaviorTree/BlackboardComponent.h"
#include "BehaviorTree/Blackboard/BlackboardKeyAllTypes.h"
#include "EnemyController.h"
#include "PlayerCharacter.h"


UBTService_CheckForPlayer::UBTService_CheckForPlayer()
{
	bCreateNodeInstance = true; // add ability to create instances of this service
}

void UBTService_CheckForPlayer::TickNode(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory, float DeltaSeconds)
{
	AEnemyController* EnemyPC = Cast<AEnemyController>(OwnerComp.GetAIOwner());  // gets this enemy's AI Controller class

	if (EnemyPC)
	{
		APlayerCharacter* Player = Cast<APlayerCharacter>(GetWorld()->GetFirstPlayerController()->GetPawn()); // Search for the player
		
		if (Player)
		{
			OwnerComp.GetBlackboardComponent()->SetValue<UBlackboardKeyType_Object>(EnemyPC->PlayerKeyID, Player); // set Key ID to the player
		}
	}
}
