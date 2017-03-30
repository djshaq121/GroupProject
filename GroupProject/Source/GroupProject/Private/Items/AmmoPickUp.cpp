// Copyright LostGods

#include "GroupProject.h"
#include "AmmoPickUp.h"
#include "PlayerCharacter.h"


void AAmmoPickUp::OnInteract_Implementation(AActor* Caller)
{
	APlayerCharacter* Player = Cast<APlayerCharacter>(Caller);
	if (Player)
	{
		Player->AddAmmo(AmmoAmount, AmmoType);
	}
}

/*When the player enters collision box add ammo to their gun*/
void AAmmoPickUp::OnPlayerEnterPickupBox(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult & SweepResult)
{
	
	APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	if (Player)
	{
			Player->AddAmmo(AmmoAmount, AmmoType);
			Destroy();
	}
}
