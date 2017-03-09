// Copyright LostGods

#pragma once

#include "GameFramework/GameMode.h"
#include "WaveGameMode.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AWaveGameMode : public AGameMode
{
	GENERATED_BODY()
	
public:
	UFUNCTION(BlueprintCallable, Category = "Wave")
		void setWaveDelay(float delay);
	UFUNCTION(BlueprintCallable, Category = "Wave")
		void SetMaxWaves(int32 Max);
	UFUNCTION(BlueprintCallable, Category = "Wave")
		void SetWaveInfo(const TArray<FWaveInfo>& newWaveInfo);
	UFUNCTION(BlueprintCallable, Category = "Wave")
	int32 GetEnemiesRemaining() const;//Get the enemies remaining to be displayed on the HUD

	void UpdateHUD();

	virtual void BeginPlay() override;
	virtual void Killed(AController* Killer, AController* Victim);


protected:
	void BeginWave();
	void EndWave();
	virtual void StartMatch() override;
	virtual void EndMatch() override;
	virtual void InitGameState() override;

	void StartSpawningWave();//
	void StartSpawningEnemies();//
	void SpawnEnemy();

	/*
	*void BeginSpawning();
	void SpawnEnemies();
	*/


private:
	UPROPERTY(EditDefaultsOnly)
		FName SpawnTag;//Where the AI will being spawning
	UPROPERTY(EditDefaultsOnly)
		float WaveDelay;
	UPROPERTY(EditDefaultsOnly)
	float SpawnDelay;//Spawns enemies after a fix time
	UPROPERTY(EditDefaultsOnly)
		int32 MaxWaves;
	UPROPERTY(EditDefaultsOnly)
		TArray<struct FWaveInfo> WaveInfo;
	
	int32 EnemyToSpawn;
	int32 EnemiesSpawned; //To see how much enemies already spawned
	FTimerHandle WaveTimerHandle;
	FTimerHandle SpawnTimerHandle;
	TArray<int32> SpawnedOfType;//Keeps track of how many of each type spawned
	TArray<AActor*> AISpawnPoints;
	int32 EnemiesLeftToKill;//This is used to determine if there are enemies still left to spawn 

	class AWaveGameState* WaveGS;

	
	
};
