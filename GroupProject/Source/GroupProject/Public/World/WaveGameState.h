// Copyright LostGods

#pragma once

#include "GameFramework/GameState.h"
#include "WaveGameState.generated.h"

/**
 * This class holds all the information about the state the game is in. e.g. how many enemies are left
 */

UCLASS()
class GROUPPROJECT_API AWaveGameState : public AGameState
{
	GENERATED_BODY()

public:		
	
	void SetIsWaveActive(bool newActive);
	void AddEnemiesRemaining(int32 Amount);
	void SetWaveDelay(float delay);
	void SetMaxWaves(int32 Waves);
	void SetCurrentWave(int32 Wave);

	UFUNCTION(BlueprintCallable, Category = "Wave")
	bool GetIsWaveActive() const;
	UFUNCTION(BlueprintCallable, Category = "Wave")
	int32 GetEnemiesRemaining() const;
	UFUNCTION(BlueprintCallable, Category = "Wave")
		float GetWaveDelay() const;
	UFUNCTION(BlueprintCallable, Category = "Wave")
	void GetWaves(int32& Max, int32& Current) const;


	int32 GetMaxWaves() const;
	int32 GetCurrentWave() const;

		//Check when the wave is active 
	UPROPERTY(Replicated)
	bool bIsWaveActive = true;

private:

UPROPERTY(Replicated)
int32 EnemiesRemaining;

UPROPERTY(Replicated)
float TimeBetweenWaves;

UPROPERTY(Replicated)
int32 MaxWaves;

UPROPERTY(Replicated)
int32 CurrentWave;
	
	
};
