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
		class AAssaultRifleBase* AssaultRifle;

		UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Plyaer")
		class ALaserRifleBase* LaserRifle;
};