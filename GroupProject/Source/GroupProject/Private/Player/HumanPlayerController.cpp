// Copyright 

#include "GroupProject.h"
#include "HumanPlayerController.h"
#include "PlayerCharacter.h"


void  AHumanPlayerController::SetPawn(APawn* InPawn)
{
	Super::SetPawn(InPawn);
	if (InPawn)//Check is the player is there
	{
		auto PossessedPlayer = Cast<APlayerCharacter>(InPawn);
		if (!ensure(PossessedPlayer)) { return; }

		//Subscribe our local methods to the players deaths
		PossessedPlayer->OnDeath.AddUniqueDynamic(this, &AHumanPlayerController::OnPossesPlayerDeath);
	}
}


void AHumanPlayerController::OnPossesPlayerDeath()
{
	//StartSpectatingOnly();//When the player dies go into spectating mode 
	//Make 
	Destroy();
}

void AHumanPlayerController::BeginPlay()
{
	Super::BeginPlay();

	//Finding the player and checking if the controller is possing the player
	auto ControlledPlayer = GetPawn();
	if (!ControlledPlayer)
	{
		UE_LOG(LogTemp, Warning, TEXT("Not possing player"))
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("Possing player"))
	}
}


void AHumanPlayerController::Tick(float DeltaSeconds)
{
}






