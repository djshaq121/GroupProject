// Fill out your copyright notice in the Description page of Project Settings.

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "GroupProjectGameMode.h"


AGroupProjectGameMode::AGroupProjectGameMode()
{

}

void AGroupProjectGameMode::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	
	APlayerCharacter * Player = Cast<APlayerCharacter>(UGameplayStatics::GetPlayerPawn(this, 0));
	if (Player)
	{
		if (Player->GetIsDead())
		{
			SetState(EGameState::EGameOver);
			//OnDeathRequest.Broadcast();
		}

	}
	

}

EGameState AGroupProjectGameMode::GetCurrentState() const
{
	return CurrentState;
}

void AGroupProjectGameMode::SetState(EGameState NewState)
{
	CurrentState = NewState;
}