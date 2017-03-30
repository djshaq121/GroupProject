// Copyright LostGods

#include "GroupProject.h"
#include "WavePlayerState.h"

//Update Gold
void AWavePlayerState::AddGold(int32 Amount) 
{
	Gold += Amount;
}

//Update score
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

