// Copyright 

#include "GroupProject.h"
#include "AIShootingCharacter.h"
#include "PlayerCharacter.h"
#include "EnemyController.h"
#include "BehaviorTree/BehaviorTree.h"
#include "Perception/PawnSensingComponent.h"

AAIShootingCharacter::AAIShootingCharacter()
{
	PawnSensingComp = CreateDefaultSubobject<UPawnSensingComponent>(TEXT("PawnSensingComp"));
	PawnSensingComp->SetPeripheralVisionAngle(60.0f);
	PawnSensingComp->SightRadius = 2000;
	PawnSensingComp->HearingThreshold = 600;
	PawnSensingComp->LOSHearingThreshold = 1200;
}
void AAIShootingCharacter::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	/* Check if the last time we sensed a player is beyond the time out value to prevent from endlessly following a player. */
	if (bSensedTarget && (GetWorld()->TimeSeconds - LastSeenTime) > SenseTimeOut)
	{
		AEnemyController* AIController = Cast<AEnemyController>(GetController());
		if (AIController)
		{
			bSensedTarget = false;
			/* Reset */
			AIController->SetTargetEnemy(nullptr);
		}
	}
}

void AAIShootingCharacter::BeginPlay()
{
	Super::BeginPlay();

	if (PawnSensingComp)
	{
		//This is an event where if the player is seen it will call onseenplayer method
		PawnSensingComp->OnSeePawn.AddDynamic(this, &AAIShootingCharacter::OnSeePlayer);
		//If the AI hears a noise it will call the method on hear noise
		PawnSensingComp->OnHearNoise.AddDynamic(this, &AAIShootingCharacter::OnHearNoise);
	}
}

void AAIShootingCharacter::OnSeePlayer(APawn * PawnInstigator)
{
	UE_LOG(LogTemp, Warning, TEXT("I see you"))
}

void AAIShootingCharacter::OnHearNoise(APawn * PawnInstigator, const FVector & Location, float Volume)
{
	UE_LOG(LogTemp, Warning, TEXT("I hear you"))
}
