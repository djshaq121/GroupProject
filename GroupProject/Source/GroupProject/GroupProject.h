// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

/* Stencil index mapping to PP_OutlineColored */
#define STENCIL_FRIENDLY_OUTLINE 252;
#define STENCIL_NEUTRAL_OUTLINE 253;
#define STENCIL_ENEMY_OUTLINE 254;
#define STENCIL_ITEMHIGHLIGHT 255;
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
		int32 MaxAmountOfEnemyType;
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

UENUM(BlueprintType)
enum class EStencilColor : uint8
{
	SC_None = 0		UMETA(DisplayName = "Disabled"),
	SC_Green = 250 	UMETA(DisplayName = "Green"),
	SC_Blue = 251		UMETA(DisplayName = "Blue"),
	SC_Red = 252		UMETA(DisplayName = "Red"),
	SC_White = 253	UMETA(DisplayName = "White")
};


