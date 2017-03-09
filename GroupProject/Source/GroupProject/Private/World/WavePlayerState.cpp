// Copyright LostGods

#include "GroupProject.h"
#include "WavePlayerState.h"


void AWavePlayerState::AddGold(int32 Amount) 
{
	Gold += Amount;
}

void AWavePlayerState::AddScore(int32 Amount)
{
	PlayerScore += Amount;
}

int32 AWavePlayerState::GetGold() const
{
	return Gold;
}

int32 AWavePlayerState::GetScore() const
{
	return PlayerScore;
}

