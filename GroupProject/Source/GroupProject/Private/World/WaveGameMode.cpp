// Copyright LostGods

#include "GroupProject.h"
#include "WaveGameMode.h"
#include "AIEnemyMaster.h"
#include "WaveGameState.h"
#include "WavePlayerState.h"
#include "PlayerCharacter.h"


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
	WaveStart.Broadcast();
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

void AWaveGameMode::UpdateHUD()
{
	APlayerCharacter* Player = Cast<APlayerCharacter>(GetWorld()->GetFirstPlayerController()->GetPawn());
	if (Player && Player->IsPlayerControlled())
	{
		Player->UpdateHUD();
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

int32 AWaveGameMode::GetEnemiesRemaining() const
{
	return EnemiesLeftToKill;
}

void AWaveGameMode::Killed(AController * Killer, AController * Victim)
{
	
	AAIEnemyMaster* VictimPawn = Cast<AAIEnemyMaster>(Victim->GetPawn());
	if (VictimPawn && !VictimPawn->IsPlayerControlled())
	{
		WaveGS->AddEnemiesRemaining(-1);
		UpdateHUD();
	}


	AAIEnemyMaster* KilledPawn = Cast<AAIEnemyMaster>(Victim->GetPawn());
	AWavePlayerState* WavePS = Cast<AWavePlayerState>(Killer->PlayerState);
	if (WavePS)
	{
		if (KilledPawn)
		{
			WavePS->AddGold(KilledPawn->GetGoldReward());//Adds the gold 
			WavePS->AddScore(KilledPawn->GetScoreReward());//Adds the score
			KilledPawn->DetachFromControllerPendingDestroy();
			EnemiesLeftToKill--;//Once we kill an enemy reduce the amount of EnemiesLeftToKill
			UpdateHUD();
		}
		
	}

	//Checking to see if enemies left is zero & if there are still enemies left to spawn
	if (WaveGS->GetEnemiesRemaining() <= 0 && EnemiesLeftToKill <= 0)
	{
		EndWave();
	}
}


void AWaveGameMode::EndWave()
{
	
	WaveGS->SetIsWaveActive(false);
	UpdateHUD();
	if (WaveGS->GetCurrentWave() >= MaxWaves)
	{
		EndMatch();//So if wave is equal to the number of rounds end the match
	}
	else
	{
		GetWorld()->GetTimerManager().SetTimer(WaveTimerHandle, this, &AWaveGameMode::BeginWave, WaveDelay, false);//This starts the next wave after the wave delay
	}

}

void AWaveGameMode::BeginWave()
{
	WaveStart.Broadcast();
	GetWorld()->GetTimerManager().ClearTimer(WaveTimerHandle);
	WaveTimerHandle.Invalidate();

	WaveGS->SetIsWaveActive(true);
	WaveGS->SetCurrentWave(WaveGS->GetCurrentWave() + 1);//Increases the wave
	UpdateHUD();

	int32 CurrentWave = WaveGS->GetCurrentWave();
	if (WaveInfo.Num() == 0)
	{
		UE_LOG(LogTemp, Error, TEXT("Please add wave info "))
		return;
	}

	//TODO - Crashes if Max wave is greater than the fwaveInfo
	
	
	EnemiesLeftToKill = WaveInfo[CurrentWave - 1].TotalNumberOfEnemiesThisWave;//At the begining of the wave set the amount of total enemies that need to spawn 

	StartSpawningWave();


}

void AWaveGameMode::StartSpawningWave()
{
	WaveStart.Broadcast();
	SpawnedOfType.Empty();//Clear the amount of enemies 
	int32 CurrentWave = WaveGS->GetCurrentWave();
	for (int i = 0; i < WaveInfo[CurrentWave - 1].EnemySpawnInfo.Num(); i++)//This gets the different type of enemy
	{
		int num = WaveInfo[CurrentWave - 1].EnemySpawnInfo.Num();
		SpawnedOfType.Add(0);
		
	}

	
	StartSpawningEnemies();
}

void AWaveGameMode::StartSpawningEnemies()
{
	WaveStart.Broadcast();
	//Check if we can spawn enemies 
	int32 CurrentWave = WaveGS->GetCurrentWave();//Gets the current wave

	GetWorld()->GetTimerManager().SetTimer(SpawnTimerHandle,this,&AWaveGameMode::SpawnEnemy,SpawnDelay,true);//We dont want it to loop because its already in a for loop
	
	EnemiesSpawned = 0;
}

void AWaveGameMode::SpawnEnemy()
{
	if (AISpawnPoints.Num() < 1 || WaveInfo.Num() < 1)//Check to see if we have spawns point or wave info
	{
		UE_LOG(LogTemp, Error, TEXT(" No spawnpoint or WaveInfo"))
		GetWorld()->GetTimerManager().ClearTimer(SpawnTimerHandle);
		SpawnTimerHandle.Invalidate();
	}

	

	//Spawning the enemy
	int32 CurrentWave = WaveGS->GetCurrentWave();//Gets the current wave
	if (EnemiesSpawned != WaveInfo[CurrentWave - 1].TotalNumberOfEnemiesThisWave)// For some reason '<=' always spawned an extra enemy  
	{
		//Gets the class to spawn information in the struct
		FSpawnInfo SpawnInfo = WaveInfo[CurrentWave - 1].EnemySpawnInfo[EnemyToSpawn];


		//This checks how much enemy types spawned. 
		if (SpawnedOfType[EnemyToSpawn] < SpawnInfo.MaxAmountOfEnemyType)
		{

			//Probability that the AI will be spanwed 
			float Prob = FMath::RandRange(0.f, 1.f);
			if (Prob <= SpawnInfo.Probability)//So if prob is smaller than the AI probaility spawn it 
			{
				//Spawns at an random point
				int32 SpawnIndex = FMath::RandRange(0, AISpawnPoints.Num() - 1);
				FVector SpawnLoc = AISpawnPoints[SpawnIndex]->GetActorLocation();
				FRotator SpawnRot = AISpawnPoints[SpawnIndex]->GetActorRotation();

				GetWorld()->SpawnActor<AActor>(SpawnInfo.EnemyClass, SpawnLoc, SpawnRot);

				EnemiesSpawned++;//Increase the amount of enemeis spawned
				UpdateHUD();
			}
		}
		

		/*We increase the EnemyToSpawn so next time it spawns it spawn a different type of enemy in the Spawninfo*/
		if (EnemyToSpawn >= WaveInfo[CurrentWave - 1].EnemySpawnInfo.Num() - 1)
		{
			EnemyToSpawn = 0;
		}
		else
		{
		
			EnemyToSpawn++;
		}
		

		
		
	}
	else
	{//Once we are done spawning the enemies clear the timer 
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
	UpdateHUD();

}

void AWaveGameMode::EndMatch()
{
	Super::EndMatch();
	UpdateHUD();
	UE_LOG(LogTemp, Warning , TEXT("You've won the match"))
}


/*
//Dont Use
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

//Dont Use
void AWaveGameMode::SpawnEnemies()
{
if (AISpawnPoints.Num() < 1 || WaveInfo.Num() < 1)//Check to see if we have spawns point or wave info
{
UE_LOG(LogTemp, Error, TEXT(" No spawnpoint or WaveInfo"))
GetWorld()->GetTimerManager().ClearTimer(SpawnTimerHandle);
SpawnTimerHandle.Invalidate();
}

int32 CurrentWave = WaveGS->GetCurrentWave();
if (EnemiesSpawned < WaveInfo[CurrentWave - 1].TotalNumberOfEnemiesThisWave)//Check if we can spawn enemies
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
UE_LOG(LogTemp, Error, TEXT("Enemies Spawned: %d"), EnemiesSpawned)
SpawnedOfType[EnemyToSpawn]++;
WaveGS->AddEnemiesRemaining(1);//This updates thevalue
UpdateHUD();
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
*/