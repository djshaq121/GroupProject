// Fill out your copyright notice in the Description page of Project Settings.

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "GroupProjectGameMode.h"




void AGroupProjectGameMode::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	
	APlayerCharacter * Player = Cast<APlayerCharacter>(UGameplayStatics::GetPlayerPawn(this, 0));
	
	if (Player)
	{
		
			
		
	}
	else if(Player == nullptr)//Maybe find another method
	{
		SetState(EGameState::EGameOver);
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