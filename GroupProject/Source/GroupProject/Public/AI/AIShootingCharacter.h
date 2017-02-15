// Copyright 

#pragma once

#include "AI/AIEnemyMaster.h"
#include "AIShootingCharacter.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AAIShootingCharacter : public AAIEnemyMaster
{
	GENERATED_BODY()
	
public:
	AAIShootingCharacter();

	void Tick(float DeltaSeconds);

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	//Pawn senseing comp that allows the AI to see and hear
	UPROPERTY(VisibleAnywhere, Category = "AI")
	class UPawnSensingComponent* PawnSensingComp;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser);

	void SetState(EAIState NewStates);

	void AddToInventory(AWeaponBase* NewWeapon);

	void AddWeapon(AWeaponBase* NewWeapon);

	void StartWeaponFire();

	void StopWeaponFire();

protected:
	
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	TSubclassOf<AWeaponBase> StartingWeaponBlueprint;//Select the weapon in blueprint

	class AWeaponBase* CurrentWeaponon; //The AI current weapon

	/** weapons in inventory */
	TArray<class AWeaponBase*> Inventory;

private:
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	FName WeaponSocketName;
	UFUNCTION()
		void OnSeePlayer(APawn* PawnInstigator);
	UFUNCTION()
		void OnHearNoise(APawn* PawnInstigator, const FVector & Location, float Volume);

	EAIState States;
	
};
