// Copyright 

#include "GroupProject.h"
#include "AIShootingCharacter.h"
#include "PlayerCharacter.h"
#include "EnemyController.h"
#include "BehaviorTree/BehaviorTree.h"
#include "Perception/PawnSensingComponent.h"
#include "WeaponBase.h"

AAIShootingCharacter::AAIShootingCharacter()
{
	PawnSensingComp = CreateDefaultSubobject<UPawnSensingComponent>(TEXT("PawnSensingComp"));
	PawnSensingComp->SetPeripheralVisionAngle(60.0f);
	PawnSensingComp->SightRadius = 2000;
	PawnSensingComp->HearingThreshold = 600;
	PawnSensingComp->LOSHearingThreshold = 1200;

	//Setting the starting AI state to passive 
	States = EAIState::Passive;
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
			AIController->SetSeenEnemy(nullptr);
			bIsAiming = false;
			
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



/*If the AI see the enemy it will set the pawn instigator as a target and move to it */
void AAIShootingCharacter::OnSeePlayer(APawn * PawnInstigator)
{

	/* Keep track of the time the player was last sensed in order to clear the target */
	LastSeenTime = GetWorld()->GetTimeSeconds();
	bSensedTarget = true;

	UE_LOG(LogTemp, Warning, TEXT("See Player"))
	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	APlayerCharacter* SensedPawn = Cast<APlayerCharacter>(PawnInstigator);
	if (AIController)
	{
		if (SensedPawn)
		{
			bIsAiming = true;
			FVector Location = SensedPawn->GetActorLocation();
			AIController->SetSeenEnemy(SensedPawn);
			AIController->SetEnemyLastSeenLocation(Location);
		}
	
	}
}

/*If we the ai hears a noise this function is called*/
/*When this is called it gets the noise location of the pawninstigator and moves to that location*/
void AAIShootingCharacter::OnHearNoise(APawn * PawnInstigator, const FVector & Location, float Volume)
{

	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	
	if (AIController)
	{
		AIController->SetNoiseLocation(Location);
	}
}

void AAIShootingCharacter::SetState(EAIState NewStates)
{
	States = NewStates;
}



float AAIShootingCharacter::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
{


	int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero


	CurrentHealth -= DamageToApply;

	if (CurrentHealth <= 0)//Check to see if AI is dead
	{
		AIOnDeathRequest.Broadcast();
		SetIsDead(true);
		OnDeath();
	}

	if (DamageCauser)
	{
		AEnemyController* AIController = Cast<AEnemyController>(GetController());
		APlayerCharacter* Player = Cast<APlayerCharacter>(GetWorld()->GetFirstPlayerController()->GetPawn());
		if (!GetIsDead() && AIController)//If we still have an controller and is alive than set the damage dealer to target
		{
			AIController->SetSeenEnemy(Player);
			
		}

	}


	return DamageToApply;
}
bool AAIShootingCharacter::GetIsAiming() const
{
	return bIsAiming;
}


