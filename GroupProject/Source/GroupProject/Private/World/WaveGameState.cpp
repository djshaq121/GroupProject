// Copyright LostGods

#include "GroupProject.h"
#include "WaveGameState.h"
#include "Net/UnrealNetwork.h"

void AWaveGameState::SetIsWaveActive(bool newActive)
{
	bIsWaveActive = newActive;
}
void AWaveGameState::AddEnemiesRemaining(int32 Amount)
{
	EnemiesRemaining += Amount;
}
void AWaveGameState::SetWaveDelay(float delay)
{
	TimeBetweenWaves = delay;
}
void AWaveGameState::SetMaxWaves(int32 Waves)
{
	MaxWaves = Waves;
}
void AWaveGameState::SetCurrentWave(int32 Wave)
{
	CurrentWave = Wave;
}


bool AWaveGameState::GetIsWaveActive() const
{
	return bIsWaveActive;
}

int32 AWaveGameState::GetEnemiesRemaining() const
{
	return EnemiesRemaining;
}

float AWaveGameState::GetWaveDelay() const
{
	return TimeBetweenWaves;
}

void AWaveGameState::GetWaves(int32& Max, int32& Current) const
{
	Max = MaxWaves;
	Current = CurrentWave;
}


int32 AWaveGameState::GetMaxWaves() const
{
	return MaxWaves;
}
int32 AWaveGameState::GetCurrentWave() const
{
	return CurrentWave;
}

void AWaveGameState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const {
	Super::GetLifetimeReplicatedProps(OutLifetimeProps);

	DOREPLIFETIME(AWaveGameState, bIsWaveActive);
	DOREPLIFETIME(AWaveGameState, EnemiesRemaining);
	DOREPLIFETIME(AWaveGameState, CurrentWave);
	DOREPLIFETIME(AWaveGameState, MaxWaves);
	DOREPLIFETIME(AWaveGameState, TimeBetweenWaves);
}
