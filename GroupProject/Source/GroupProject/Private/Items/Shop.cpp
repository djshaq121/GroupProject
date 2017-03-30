// Copyright LostGods

#include "GroupProject.h"
#include "Shop.h"
#include "WaveGameState.h"

//Called when the player is looking at an shop object
void AShop::OnInteract_Implementation(AActor* Caller) {
	AWaveGameState* WaveGS = GetWorld()->GetGameState<AWaveGameState>();
	if (WaveGS->bIsWaveActive == true) {
		UE_LOG(LogTemp, Warning, TEXT("You cannot access the shop!"));
	}
	else {
		UE_LOG(LogTemp, Warning, TEXT("Welcome to the shop!"));
		ShopToggle.Broadcast();
	}
}