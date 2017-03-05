// Copyright LostGods

#include "GroupProject.h"
#include "WaveGameMode.h"
#include "AIEnemyMaster.h"
#include "WaveGameState.h"
#include "WavePlayerState.h"


void AWaveGameMode::InitGameState()
{
	Super::InitGameState();

	WaveGS = Cast<AWaveGameState>(GameState);
	if (WaveGS)
	{
		WaveGS->SetMaxWaves(MaxWaves);
		WaveGS->SetWaveDelay(WaveDelay);
	}
}
void AWaveGameMode::BeginPlay()
{
	Super::BeginPlay();

	TArray<AActor*> Spawns;//Gets all the spawn location in the world and filter the ones for AI

	UGameplayStatics::GetAllActorsOfClass(GetWorld(),APlayerStart::StaticClass(),Spawns); //this gets the informations and puts it into the spawn array
	for (AActor* Spawn : Spawns)
	{
		if (Spawn->ActorHasTag(SpawnTag))
		{
			AISpawnPoints.Add(Spawn);
		}
	}
}

void AWaveGameMode::setWaveDelay(float delay)
{
	WaveDelay = delay;
}

void AWaveGameMode::SetMaxWaves(int32 Max)
{
	MaxWaves = Max;
}

void AWaveGameMode::SetWaveInfo(const TArray<FWaveInfo>& newWaveInfo)
{
	WaveInfo = newWaveInfo;
}

void AWaveGameMode::Killed(AController * Killer, AController * Victim)
{
	UE_LOG(LogTemp, Error, TEXT("Enemy killed"))
	WaveGS->AddEnemiesRemaining(-1);

	AAIEnemyMaster* KilledPawn = Cast<AAIEnemyMaster>(Victim->GetPawn());
	AWavePlayerState* WavePS = Cast<AWavePlayerState>(Killer->PlayerState);
	if (WavePS)
	{
		if (KilledPawn)
		{
			WavePS->AddGold(KilledPawn->GetGoldReward());
			KilledPawn->DetachFromControllerPendingDestroy();
		}
		
	}

	if (WaveGS->GetEnemiesRemaining() <= 0)
	{
		EndWave();
	}
}

void AWaveGameMode::BeginWave()
{
	GetWorld()->GetTimerManager().ClearTimer(WaveTimerHandle);
	WaveTimerHandle.Invalidate();

	WaveGS->SetIsWaveActive(true);
	WaveGS->SetCurrentWave(WaveGS->GetCurrentWave() + 1);//Increases the wave
	BeginSpawning();


}

void AWaveGameMode::EndWave()
{
	
	WaveGS->SetIsWaveActive(false);
	if (WaveGS->GetCurrentWave() >= MaxWaves)
	{
		EndMatch();
	}
	else
	{
		GetWorld()->GetTimerManager().SetTimer(WaveTimerHandle, this, &AWaveGameMode::BeginWave, WaveDelay, false);//This starts the next wave after the wave delay
	}

}

void AWaveGameMode::BeginSpawning()
{
	SpawnedOfType.Empty();//Clear the amount of enemies 
	int32 CurrentWave = WaveGS->GetCurrentWave();
	for (int i=0;i < WaveInfo[CurrentWave-1].EnemySpawnInfo.Num();i++)
	{
		SpawnedOfType.Add(0);
	}
	EnemyToSpawn = 0;//Reset the values
	EnemiesSpawned = 0;

	GetWorld()->GetTimerManager().SetTimer(SpawnTimerHandle, this, &AWaveGameMode::SpawnEnemies, SpawnDelay, true);

}

void AWaveGameMode::SpawnEnemies()
{
	if (AISpawnPoints.Num() < 1 || WaveInfo.Num() < 1)//Check to see if we have spawns point or wave info
	{
		UE_LOG(LogTemp, Error, TEXT(" No spawnpoint or WaveInfo"))
		GetWorld()->GetTimerManager().ClearTimer(SpawnTimerHandle);
		SpawnTimerHandle.Invalidate();
	}

	int32 CurrentWave = WaveGS->GetCurrentWave();
	if (EnemiesSpawned < WaveInfo[CurrentWave - 1].TotalNumberOfEnemies)//Check if we can spawn enemies
	{
		FSpawnInfo SpawnInfo = WaveInfo[CurrentWave - 1].EnemySpawnInfo[EnemyToSpawn];
		if (SpawnedOfType[EnemyToSpawn] < SpawnInfo.MaxAmountOfEnemies)//if the amount of enemies we spawn of this type is less than the max enemies it spawns more
		{
			float prob = FMath::RandRange(0.f,1.f);
			if (prob <= SpawnInfo.Probability)
			{
				int32 SpawnIndex = FMath::RandRange(0, AISpawnPoints.Num() - 1);
				FVector SpawnLoc = AISpawnPoints[SpawnIndex]->GetActorLocation();
				FRotator SpawnRot = AISpawnPoints[SpawnIndex]->GetActorRotation();

				GetWorld()->SpawnActor<AActor>(SpawnInfo.EnemyClass, SpawnLoc, SpawnRot);
				EnemiesSpawned++;
				SpawnedOfType[EnemyToSpawn]++;
				WaveGS->AddEnemiesRemaining(1);//This updates thevalue
			}
		}

		if (EnemyToSpawn >= WaveInfo[CurrentWave - 1].EnemySpawnInfo.Num()-1)
		{
			EnemyToSpawn = 0;
		}
		else
		{
			EnemyToSpawn++;
		}
	}
	else
	{
		GetWorld()->GetTimerManager().ClearTimer(SpawnTimerHandle);
		SpawnTimerHandle.Invalidate();
	}

}

void AWaveGameMode::StartMatch()
{
	if (!HasMatchStarted()) {
		EndWave();//This gives the player time at the start
	}

	Super::StartMatch();
}

void AWaveGameMode::EndMatch()
{
	Super::EndMatch();
	UE_LOG(LogTemp, Warning , TEXT("You've won the match"))
}


