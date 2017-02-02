// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "GameFramework/GameMode.h"
#include "GroupProjectGameMode.generated.h"

/**
 * 
 */


 //Expose this to blueprint
 /*Keeps track of the state of the game*/
UENUM(BlueprintType)
enum class EGameState : uint8
{
	EMenu,
	EPlaying,
	EGameOver,
	EUnknown

};

UCLASS()
class GROUPPROJECT_API AGroupProjectGameMode : public AGameMode
{
	GENERATED_BODY()
	
public:


	//Called every frame
virtual void Tick(float DeltaSeconds) override;
	

UFUNCTION(BlueprintCallable, Category = "State")
EGameState GetCurrentState() const;

UFUNCTION(BlueprintCallable, Category = "State")
void SetState(EGameState NewState);

private:


/*Keeps track of the state of the game*/
EGameState CurrentState;
	
};
