// Copyright LostGods

#pragma once

#include "BehaviorTree/BTService.h"
#include "BTUpdateEnemyLastSeenLocation.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API UBTUpdateEnemyLastSeenLocation : public UBTService
{
	GENERATED_BODY()
	
	
public:
	virtual void TickNode(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory, float DeltaSeconds) override;


	
};
