// Copyright LostGods

#include "GroupProject.h"
#include "WavePlayerState.h"


void AWavePlayerState::AddGold(int32 Amount) 
{
	Gold += Amount;
}

int32 AWavePlayerState::GetGold() const
{
	return Gold;
}

