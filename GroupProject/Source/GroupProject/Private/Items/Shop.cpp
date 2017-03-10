// Copyright LostGods

#include "GroupProject.h"
#include "Shop.h"
#include "WaveGameState.h"


void AShop::OnInteract_Implementation(AActor* Caller) {
	AWaveGameState* WaveGS = GetWorld()->GetGameState<AWaveGameState>();
	if (WaveGS->bIsWaveActive == true) {
		UE_LOG(LogTemp, Warning, TEXT("You cannot access the shop!"));
	}
	else {
		UE_LOG(LogTemp, Warning, TEXT("Welcome to the shop!"));
	}
}