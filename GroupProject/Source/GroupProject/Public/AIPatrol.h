// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "AIPatrol.generated.h"


UCLASS()
class GROUPPROJECT_API AAIPatrol : public ACharacter
{
	GENERATED_BODY()

public:
	// Sets default values for this character's properties
	AAIPatrol();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* InputComponent) override;

	UPROPERTY(EditAnywhere, Category = AI)
		class UBehaviorTree* BehaviorTree;

	UPROPERTY(VisibleAnywhere, Category = AI)
		class UPawnSensingComponent* PawnSensingComp;
private:

	UFUNCTION()
		void OnPlayerCaught(APawn* Pawn);

};
