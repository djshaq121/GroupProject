// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#define ECC_Weapon ECC_GameTraceChannel1

#include "Engine.h"
#include "GroupProject.generated.h"

USTRUCT(BlueprintType)
struct FPlayerInventory
{
	GENERATED_USTRUCT_BODY()

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class AWeaponBase* CurrentWeapon;

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class AWeaponBase* PreviousWeapon;

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class AAssaultRifleBase* AssaultRifle;

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class ALaserRifleBase* LaserRifle;

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class APistolBase* Pistol;
};

UENUM(BlueprintType)
enum class EAmmoType : uint8
{
	//GENERATED_USTRUCT_BODY()

	AT_Bullets UMETA(DisplayName="Assault"),
	AT_Pistol UMETA(DisplayName = "Pistol"),
	AT_Lasers UMETA(DisplayName = "LaserRifle")
};

USTRUCT(BlueprintType)
struct FSpawnInfo
{
	GENERATED_USTRUCT_BODY()

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Spawning")
		TSubclassOf<class AAIEnemyMaster> EnemyClass;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Spawning")
		int32 MaxAmountOfEnemies;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Spawning")
		float Probability;
};

USTRUCT(BlueprintType)
struct FWaveInfo
{
	GENERATED_USTRUCT_BODY()

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Spawning")
		int32 TotalNumberOfEnemiesThisWave; //The Max number of enemies 
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Spawning")
		TArray<FSpawnInfo> EnemySpawnInfo;
};